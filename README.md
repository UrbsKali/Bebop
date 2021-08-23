# Update : pyparrot does NOT work with the new firmware of the bebop 2, so this repo is useless until I have the motivation to update pyparrot

# Bebop Control Script
Some useful python script which allows you to control your parrot bebop 2 with code, get live stream, and schedule routes! 
<br>
# How to use ?
First, you will need to install the <a href="#Dependencies">dependencies</a>. Secondly, for each script, you have a notice inside file and a sum in this readme.
You have to connect your computer to your drone's wifi before begin to use the code in order to make your bebop fly !<br> 
Content : <br>
<a href="#Bebop_cmd">Bebop_cmd.py</a>
<br>
# Dependencies

You <strong>must</strong> have install <strong>pyparrot</strong>, To do that, you can install manually or lauch the setup.py script
<br>
# Bebop_cmd
connect(): this command give you the power of all the following command, so do it first.<br>
disconnect() : disconnect your drone from all python commands.<br>
take(number_of_seconde) : make your bebop 2 take in a certain number of seconde (default : 5).<br>
land(number_of_seconde) : make your bebop 2 land in a certain number of seconde (default: 5).<br>
fow(power, duration) : make your drone go foward, the power must take values between -100 and 100 (default : 20, 1).<br>
back(power, duration) : make your drone go backward, the power must take values between -100 and 100 (default : 20, 1).<br>
left(power, duration) : make your drone go left, the power must take values between -100 and 100 (default : 10, 1).<br>
right(power, duration) : make your drone go right, the power must take values between -100 and 100 (default : 10, 1).<br>
r_left(degre, duration) : make your drone turn left, the degre must take values between -100 and 100 (default : 10, 1).<br>
r_right(degre, duration) : make your drone turn right, the degre must take values between -100 and 100 (default : 10, 1).<br>


# License 

This work is under the GNU GPL v3.0 license, so please give me the credit if you want to fork or uprgade ! 
<br>
Thank you for reading !<br>
