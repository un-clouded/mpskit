mpskit
======

Madspack file format decoder/encoder for Rex Nebular, Dragonsphere, Colonization and other Microprose games. Can run on Linux or Windows (using Cygwin).

Version 1.4.0

Release Notes
-------------

**1.4.0** - Rex Nebular ART format support added; All png files are now written in indexed mode (see Notes below)

**1.3.0** - MESSAGES.DAT is now unpacked/packed into/from 2 files: MESSAGES.DAT.msg.json and MESSAGES.DAT.id.json. 
If you have modified MESSAGES.DAT.msg.json you will need to pair it up with MESSAGES.DAT.id.json extracted from unmodified MESSAGES.DAT


Installation
------------

1) Install dependencies

* On Debian run `sudo apt-get install python3-pil`
* On Windows install Cygwin (http://cygwin.com/install.html) with following packages (select them during install): wget, python3, python3-imaging, unzip, chere

2) Open terminal (Cygwin terminal on Windows) and run following commands:

```bash

# download
wget -O mpskit.zip https://github.com/institution/mpskit/archive/master.zip
unzip -o master.zip
cd mpskit-master

# install in system path
echo "python3 `pwd`/main.py \$*" > /usr/local/bin/mpskit
chmod +x /usr/local/bin/mpskit

# test - should display usage
mpskit

# optional Windows step: add "Open terminal here" option to Windows Explorer
chere -i -t mintty

```


Supported File Formats
----------------------

|command  |applied to                            |content             |
|---------|--------------------------------------|--------------------|
|hag      |HAG files                             |collection of files |
|mdat     |MESSAGES.DAT file                     |text                |
|rdat     |DAT files containing text             |text                |
|ss       |SS files                              |sprites             |
|aa       |AA files                              |text                |
|cnv      |CNV files                             |text                |
|art      |ART files                             |background image    |
|ff       |FF files                              |glyphs              |
|pik      |PIK files                             |background image    |
|fab      |file containing FAB section           |                    |
|madspack |any file which begins with "MADSPACK" |                    |



Usage examples
--------------

### General usage ###
	
	cd REX
	
	# unpacking
	mpskit hag unpack GLOBAL.HAG	
	mpskit mdat unpack GLOBAL.HAG.dir/MESSAGES.DAT
	mpskit ss unpack GLOBAL.HAG.dir/*.SS

	# now you can modify generated txt and png files

	# packing
	mpskit ss pack GLOBAL.HAG.dir/GRD1_2.SS
	mpskit mdat pack GLOBAL.HAG.dir/MESSAGES.DAT	
	mpskit hag pack GLOBAL.HAG
	

### Changing AA messages ###

	# unpack
	mpskit hag unpack SECTION9.HAG
	mpskit aa unpack SECTION9.HAG.dir/RM951A.AA

Now in `SECTION9.HAG.dir/RM951A.AA.msg.json`
	
	change this:
	"msg": "\"Here it is, Stone."
	
	to this:
	"msg": "\"Hello, Kitty!"      

	pos_x can be changed to adjust text position on the screen
    "pos_x": 159,


### Modify CNV message ###

	mpskit hag unpack GLOBAL.HAG
	mpskit cnv unpack GLOBAL.HAG.dir/CONV000.CNV
	
	# now modify GLOBAL.HAG.dir/CONV000.CNV.msg.json
	
	mpskit cnv pack GLOBAL.HAG.dir/CONV000.CNV
	mpskit hag pack GLOBAL.HAG


### Adding new letter to font ###

	cd GLOBAL.HAG.dir	
	mpskit ff unpack FONTCONV.FF
	cp FONTCONV.FF.099.png FONTCONV.FF.001.png
	
	# edit your new letter but do not insert new colors to the image
	# modifying image width is ok
	gimp FONTCONV.FF.001.png
		
	mpskit ff pack FONTCONV.FF
	mpskit hag pack ../GLOBAL.HAG
	
### Unpack all supported files ###

	mpskit hag unpack *.HAG
	mpskit ss unpack */*.SS
	mpskit ff unpack */*.FF
	mpskit aa unpack */*.AA
	mpskit cnv unpack */*.CNV
	mpskit art unpack */*.ART
	mpskit pik unpack */*.PIK


Notes
-----

* png files are written in indexed mode with embeded palette ("Colormap" dialog in GIMP)
* changes to embeded palette are ignored by mpskit
* use "mdat" for MESSAGES.DAT and "rdat" for other .DAT files

License
-------
AGPLv3 or later

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Contact
-------
sta256+mpskit@gmail.com

Thanks to
---------
ScummVM Project (http://scummvm.org/)







