# Registers tyleryeedu@gmail.com as a verified SES sending identity.
# AWS will send a verification email to this address — click the link before
# attempting to send any emails from Lambda.
#
# Note: new SES accounts start in sandbox mode. In sandbox, you can only send
# TO verified addresses as well. To send to any address, request production
# access in the AWS console: SES → Account dashboard → Request production access.

resource "aws_sesv2_email_identity" "sender" {
  email_identity = var.sender_email
}
