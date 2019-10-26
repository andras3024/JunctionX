from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework_jwt.settings import api_settings
from django.urls import reverse


# ===========================================================
# Show QR code view for admin.
# ===========================================================
@api_view(["GET"])
@login_required
def show_qrcode(request,  **kwargs):
    # Generate JSON web token for user
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(request.user)
    access_token = jwt_encode_handler(payload)
    qr_text = '{0}/{1}'.format(str(request.build_absolute_uri()), access_token)
    # Create context for html file
    context = {
        'title': 'QR code',
        'qr_text': str(qr_text),
               }

    return render(request, 'qrcode_app/qr.html', context)

