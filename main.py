import subprocess

def wizard():
    try:
        print("Welcome to the NvidiaAIDenoiser Automation Wizard.\nMade by TYX8926 as supplement of DeclanRussell's NvidiaAIDenoiser program\nOriginal program: https://github.com/DeclanRussell/NvidiaAIDenoiser")

        print()
        print("Make sure the denoiser program is added to PATH before continuing,\nand that the file names are in numerical order (e.g. img0.png, img1.png).")

        print()

        print("Please specify the following...")
        path = input("Path to files (Optional; put slash at the end if specified): ").replace("\\", "/").replace("\"", "")
        outputPath = input("Output folder (Optional; put slash at the end if specified): ").replace("\\", "/").replace("\"", "")
        rangeImgR = input("Range of files to denoise (Number following the prefix; comma-separated): ")
        prefix = input("Filename prefix (Optional): ")
        suffix = input("Filename suffix (Optional): ")

        # I completely forgot how to do this properly.

        rangeImg = rangeImgR.split(",")
        x = int(rangeImg[0])
        y = int(rangeImg[1])

        count = x

        print()
        print("Starting batch denoise...")

        for i in range((y - x) + 1):
            combined = path + prefix + suffix + str(count)
            subprocess.run(["Denoiser", "-i", (combined + ".png"), "-o", (combined + outputPath + "_denoised.png")])
            count += 1
            print()
        
        input("Finished! Press any key to exit...")
    except KeyboardInterrupt:
        print("\n\nExiting...")

wizard()
exit()
