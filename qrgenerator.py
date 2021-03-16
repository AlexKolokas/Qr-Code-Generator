import qrcode
# ask the user to give the informations for the qrcode
print('Enter your site or text')
input_data =input()

#Creating an instance of qrcode
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5,
        )

qr.add_data(input_data)
qr.make(fit=True)
#colors for the qrcode
img = qr.make_image(fill_color='black', back_color='white')
#ask the user to give the saving name of the qrcode
print('Give the name for your file. exp:qrcode.png')
inputfilename=input()
#adds a .png to the saving name (so the qrcode is saved as png)
inputfilenamefinal=inputfilename+'.png'
img.save(inputfilenamefinal) #save the qr code as png
