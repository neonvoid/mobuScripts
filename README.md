# mobuScripts

I'll update this more
Right now the script is not flexible at all lol, but i'll write down instructions and document steps to do in mobu prior to using the script.

Or I'll try to automate that part too cause it's just a bunch of clicking right now.
Unreal requires your import to have a skeleton bound to it, it doesn't have to be skinned so binding even just a cube to the motion data is good enough.

That's all the script does really, grabs 5 poitns around the body from an imported xml and then parents a cube to it. 

Then you can just use the unreal IK retargetter to do the rest.

I used Mocappys example script as a really helpful base and for xml parsing and the pyfbsdk.

https://mocappys.com/how-to-t-pose-and-characterize-your-character-using-motionbuilder-python/#.Y_UQx3bMIQ8
