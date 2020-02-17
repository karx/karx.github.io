## To upload code to Home Switch Devices
Abacus Services

### Step 1 Setting Up Environment
* Install Python
* Install esptools.py
```
pip install esptool
```
* Download latest code zip

### Step 2 Hardware


### Step 3 Upload

```
esptool.py --port /dev/cu.SLAB_USBtoUART write_flash 0x10000 _c_0x10000.bin
```
