# msfs-script-bucket.
Helpful scripts to make your MSFS more enjoyable.

## How to convert ivao_x-csl aircraft to Live Traffic

Note: This is not the cleanest script I have ever written but it works. This purely relies on a "happy path" for the ivao_x-csl aircraft for MSFS.
Note: I can not garuntee this will work if you have modified the airplanes aircraft.cfg in any way.

## Steps
0. Install the latest version of python. Make sure you enable the setting in the wizard to update the PATH.
1. Downoad the package from [IVAO](https://www.ivao.aero/softdev/beta/altitudebeta.asp) (you may need to register for an account).
2. Follow instructions to install.
3. Try to make a backup of the .zip package once download is complete. If not, make a backup of the ivao_x-sl folder located inside your community folder. (make sure backup is outside of your community directory.
4. Place the python script inside `Community\ivao_x-csl\SimObjects\Airplanes` folder.
5. Double click on the python file or open Powershell and run `python C:\Users\$USERNAME\AppData\Local\Packages\Microsoft.FlightSimulator_8wekyb3d8bbwe\LocalCache\Packages\Community\ivao_x-csl\SimObjects\Airplanes` not this may be different for steam users and replace *$USERNAME* with your actualy username on pc.
6. Launch flightsim and enjoy.
7. Report bugs back to me under the issues tab!

I'm so very excited to contribute to the flightsim community and I hope this script will change the experience of many. I haven't tested everything but as a community we can try to make this solution a bit better until Asobo/3rd party releases something better.

- Kai
