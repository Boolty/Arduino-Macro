import os, time
from check_access import check_access

def replace_in_file(user_name):
    access_granted, message = check_access()
    print(message)
    if access_granted:
        # Pfad zur Datei 'boards.txt'
        path = f'C:\\Users\\{user_name}\\AppData\\Local\\Arduino15\\packages\\arduino\\hardware\\avr\\1.8.6\\boards.txt'

        # Überprüfen, ob die Datei existiert
        if not os.path.exists(path):
            print("Die Datei existiert nicht.")
            return

        # Zu ersetzender Inhalt
        old_content = """
    leonardo.name=Arduino Leonardo
    leonardo.vid.0=0x2341
    leonardo.pid.0=0x0036
    leonardo.vid.1=0x2341
    leonardo.pid.1=0x8036
    leonardo.vid.2=0x2A03
    leonardo.pid.2=0x0036
    leonardo.vid.3=0x2A03
    leonardo.pid.3=0x8036
    leonardo.upload_port.0.vid=0x2341
    leonardo.upload_port.0.pid=0x0036
    leonardo.upload_port.1.vid=0x2341
    leonardo.upload_port.1.pid=0x8036
    leonardo.upload_port.2.vid=0x2A03
    leonardo.upload_port.2.pid=0x0036
    leonardo.upload_port.3.vid=0x2A03
    leonardo.upload_port.3.pid=0x8036
    leonardo.upload_port.4.board=leonardo
    
    leonardo.upload.tool=avrdude
    leonardo.upload.tool.default=avrdude
    leonardo.upload.tool.network=arduino_ota
    leonardo.upload.protocol=avr109
    leonardo.upload.maximum_size=28672
    leonardo.upload.maximum_data_size=2560
    leonardo.upload.speed=57600
    leonardo.upload.disable_flushing=true
    leonardo.upload.use_1200bps_touch=true
    leonardo.upload.wait_for_upload_port=true
    
    leonardo.bootloader.tool=avrdude
    leonardo.bootloader.tool.default=avrdude
    leonardo.bootloader.low_fuses=0xff
    leonardo.bootloader.high_fuses=0xd8
    leonardo.bootloader.extended_fuses=0xcb
    leonardo.bootloader.file=caterina/Caterina-Leonardo.hex
    leonardo.bootloader.unlock_bits=0x3F
    leonardo.bootloader.lock_bits=0x2F
    
    leonardo.build.mcu=atmega32u4
    leonardo.build.f_cpu=16000000L
    leonardo.build.vid=0x2341
    leonardo.build.pid=0x8036
    leonardo.build.usb_product="Arduino Leonardo"
    leonardo.build.board=AVR_LEONARDO
    leonardo.build.core=arduino
    leonardo.build.variant=leonardo
    leonardo.build.extra_flags={build.usb_flags}
    """

        new_content = """
    pario.name=Pario
    pario.vid.0=0x7999
    pario.pid.0=0x7999
    pario.vid.1=0x7998
    pario.pid.1=0x7998
    pario.vid.2=0x7997
    pario.pid.2=0x7997
    pario.vid.3=0x7996
    pario.pid.3=0x7996
    pario.upload_port.0.vid=0x7999
    pario.upload_port.0.pid=0x7999
    pario.upload_port.1.vid=0x7998
    pario.upload_port.1.pid=0x7998
    pario.upload_port.2.vid=0x7997
    pario.upload_port.2.pid=0x7997
    pario.upload_port.3.vid=0x7996
    pario.upload_port.3.pid=0x7996
    pario.upload_port.4.board=leonardo
    
    pario.upload.tool=avrdude
    pario.upload.tool.default=avrdude
    pario.upload.tool.network=arduino_ota
    pario.upload.protocol=avr109
    pario.upload.maximum_size=28672
    pario.upload.maximum_data_size=2560
    pario.upload.speed=57600
    pario.upload.disable_flushing=true
    pario.upload.use_1200bps_touch=true
    pario.upload.wait_for_upload_port=true
    
    pario.bootloader.tool=avrdude
    pario.bootloader.tool.default=avrdude
    pario.bootloader.low_fuses=0xff
    pario.bootloader.high_fuses=0xd8
    pario.bootloader.extended_fuses=0xcb
    pario.bootloader.file=caterina/Caterina-Leonardo.hex
    pario.bootloader.unlock_bits=0x3F
    pario.bootloader.lock_bits=0x2F
    
    pario.build.mcu=atmega32u4
    pario.build.f_cpu=16000000L
    pario.build.vid=0x7999
    pario.build.pid=0x7999
    pario.build.usb_product="pario"
    pario.build.board=AVR_LEONARDO
    pario.build.core=arduino
    pario.build.variant=leonardo
    pario.build.extra_flags={build.usb_flags}
    """

        # Datei lesen und Inhalt ersetzen
        try:
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()

            if old_content in content:
                content = content.replace(old_content, new_content)
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(content)
                print("Der Inhalt wurde erfolgreich ersetzt.")
                time.sleep(5)
            else:
                print("Der spezifizierte Text wurde in der Datei nicht gefunden.")
                time.sleep(5)
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")
            time.sleep(5)

    # Nutzername dynamisch einsetzen
    import getpass
    user_name = getpass.getuser()
    replace_in_file(user_name)
