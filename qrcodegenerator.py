import qrcode
# Link for website
userinput = input("your link : ")
input_data = userinput
#Creating an instance of qrcode
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
name = input("name of the file : ")
img.save(name + ".png")
