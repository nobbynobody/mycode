#%%
#!/usr/bin/env python3

import requests
import crayons

#define datasource
DATASRC="https://api.spacexdata.com/v3/dragons"

def main():
    sdata = requests.get(DATASRC)

    #check request status
    if sdata.status_code == 200:       
        dragondata = sdata.json()
        for dragon in dragondata:
            dragonname = (dragon.get("name"))
            dragonmass = (dragon.get("dry_mass_kg"))
            dragonplwt = (dragon.get("launch_payload_mass").get("kg"))
            
            print(f"Dragon name: {crayons.blue(dragonname)}")

            #is it heavy?
            if dragonmass > 6000:                
                print(f"Dragon dry mass: {crayons.red(dragonmass)} Wow! That's Heavy!")
            else:
                print(f"Dragon dry mass: {crayons.yellow(dragonmass)}")
            print(f"Dragon payload weight: {crayons.magenta(dragonplwt)}")
            print()
            
    else:
        print("Error with request")

if __name__ == "__main__":
    main()

