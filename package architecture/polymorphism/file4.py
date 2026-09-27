from typing_extensions import override
class Whatsup1:
    def send_message(self):
        print("single tick supported")

class Whatsup2(Whatsup1):
    @override                   #overide method
    def send_message(self):
        super().send_message()
        print("double tick supported")

    def send_audio(self):       #normal instance method
        print("audio message sent")

class Whatsup3(Whatsup2):
    @override
    def send_message(self):
        super().send_message()
        print("blue tick supported")

    @override
    def send_audio(self):       #normal instance method
        super().send_audio()
        print("enhanced audio message sent")


    def send_video(self):       #normal instance method
        print("video message sent")


w=Whatsup3()
w.send_message()
w.send_audio()
w.send_video()

print(Whatsup3.__mro__)



