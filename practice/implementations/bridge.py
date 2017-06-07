#We have a linux machine and a windows machine
#We are testing their capabilities, and we need to verify both can send emails and telnet messages
#We need to send a notification to another machine from both linux and windows machines

message = "Automated notification: Hello!"
target_mail = "target@mail.com"
target_telnet = "telnet_address"

#We have different notificators and different platforms, so it makes sense to separate them
class WindowsEmailNotificator:
    def send_mail(self,email,message):
        print('Using windows specific email handling')
        print('Sent email to {}'.format(email))

class LinuxEmailNotificator:
    def send_mail(self, email, message):
        print('Using linux specific email handling')
        print('Sent email to {}'.format(email))

class WindowsTelnetNotificator:
    def send_telnet(self,address,message):
        print('Using windows specific telnet handling')
        print('Sent telnet message to {}'.format(address))

class LinuxTelnetNotificator:
    def send_telnet(self, address, message):
        print('Using linux specific telnet handling')
        print('Sent telnet message to {}'.format(address))



print('\nNotifying with a lot of classes\n')
print('Sending mail from windows')
win_email_notificator = WindowsEmailNotificator()
win_email_notificator.send_mail(target_mail, message)

print('Sending telnet from windows')
win_telnet_notificator = WindowsTelnetNotificator()
win_telnet_notificator.send_telnet(target_telnet, message)

print('Sending mail from linux')
linux_email_notificator = LinuxEmailNotificator()
linux_email_notificator.send_mail(target_mail, message)

print('Sending telnet from linux')
linux_telnet_notificator = LinuxTelnetNotificator()
linux_telnet_notificator.send_telnet(target_telnet, message)

#This code is ugly, repetetive, tied to implementation
#We can do better with bridge pattern!


class NotificatorInterface: #The target interface 

    def notify(self, address, message):
        pass

class Bridge(NotificatorInterface): #The bridge between the target interface and the background implementation
    def __init__(self):
        self.__implementation = None

class EmailNotificator(Bridge):
    def __init__(self, implementation):
        self.__implementation = implementation

    def notify(self, address, message):
        return self.__implementation.send_mail(address, message)

class TelnetNotificator(Bridge):
    def __init__(self, implementation):
        self.__implementation = implementation

    def notify(self, address, message):
        return self.__implementation.send_telnet(address, message)


class NotifierImplementation: #abstract notifier implementation

    def send_mail(self, address, message):
        pass

    def send_telnet(self, address, message):
        pass


class Linux(NotifierImplementation):
    def send_mail(self, email, message):
        print('Using linux specific email handling')
        print('Sent email to {}'.format(email))

    def send_telnet(self, address, message):
        print('Using linux specific telnet handling')
        print('Sent telnet message to {}'.format(address))

class Windows(NotifierImplementation):
    def send_mail(self,email,message):
        print('Using windows specific email handling')
        print('Sent email to {}'.format(email))

    def send_telnet(self,address,message):
        print('Using windows specific telnet handling')
        print('Sent telnet message to {}'.format(address))

print('\nNotifying with bridge\n')

linux = Linux()
windows = Windows()

email_notificator = EmailNotificator(windows)
email_notificator.notify(target_mail, message)
email_notificator = EmailNotificator(linux)
email_notificator.notify(target_mail, message)

telnet_notificator = TelnetNotificator(windows)
telnet_notificator.notify(target_telnet, message)
telnet_notificator = TelnetNotificator(linux)
telnet_notificator.notify(target_telnet, message)




