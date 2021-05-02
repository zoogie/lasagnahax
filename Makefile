HAXNAME := payload

all:	payload.bin

clean:
	rm -f $(HAXNAME).elf payload.bin

payload.bin: $(HAXNAME).elf
	arm-none-eabi-objcopy -O binary $(HAXNAME).elf payload.bin

$(HAXNAME).elf:	$(HAXNAME).s
	arm-none-eabi-gcc -x assembler-with-cpp -nostartfiles -nostdlib -Ttext=0x002312e0 $< -o $(HAXNAME).elf

