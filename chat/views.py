from django.shortcuts import render
from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer
# from django.core.files import File
# Create your views here.
def chat(request):
    return render(request, "home.html")


class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer



# def create_message_with_attachment(request):
#     if request.method == 'POST':
#         # Get the message content from the form or request data
#         message_content = request.POST.get('content')
        
#         # Get the attachment file from the form or request data
#         attachment_file = request.FILES.get('attachment')

#         if message_content:
#             # Create a new message
#             message = Message(content=message_content)

#             if attachment_file:
#                 # Save the attachment to AWS S3
#                 message.attachment.save(attachment_file.name, File(attachment_file))

#             # Save the message
#             message.save()
            
#             # You can add a success message or redirect to a success page
#             return render(request, 'success.html', {'message': 'Message created successfully'})
    
#     # Handle GET requests or form rendering here
#     return render(request, 'message_form.html')