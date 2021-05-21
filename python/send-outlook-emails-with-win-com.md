# Problem

Using an SMTP approach to emails may fail due to a variety reasons like corporate networking barriers.

# Solution

As long as you have Outlook installed on the machine running the program, you can use Windows COM to directly control Outlook to send emails from your user account.

# Code

```python
import win32com.client as win32

def send_email(to=None, subject=None, body=None, html=False):
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = to
    mail.Subject = subject
    
    if html:
        mail.HTMLBody = body
    else:
        mail.Body = body
    
    mail.Send()
    
    
message_no_html = {'to': 'paulz@domain.com',
                   'subject': 'Foo',
                   'body': """Hi. This is the body of the email.""",
                  }

message_html = {'to': 'paulz@domain.com',
                'subject': 'Bar',
                'body': """
                           Style me with HTML.

                           <h1>Here is a header</h1>
                           <li> list item 1 </li>
                           <li> list item 2 </li>
                           <li> list item 3 </li>
                             """                
               }

send_email(**message_no_html)
send_email(**message_html, html=True)
```
