Import("env")

MCU = ["-mcpu=cortex-m7", "-mthumb", "-mfpu=fpv5-d16", "-mfloat-abi=hard"]
OPT = ["-O3"]
C_DEFS = ["-DSTM32H750xx"]

# General options that are passed to the C compiler (C only; not C++).
env.Append(
    CFLAGS = [
        "-std=gnu11"
    ]
)
# General options that are passed to the C and C++ compilers
env.Append(
    CCFLAGS=[
        *MCU,
        *C_DEFS,
        # *C_INCLUDES,
        *OPT,

        # warnings
        "-Wall",
        "-Werror",
        
        # stuff..?
        "-fdata-sections",
        "-ffunction-sections",
    ]
)
# General options that are passed to the C++ compiler (C++ only; not C).
env.Append(
    CXXFLAGS=[
        "-std=gnu++14",
        "-fno-exceptions",  
        "-finline-functions"
    ]
)
# print("printing env:")
# print(env)
# print(env.Dump())

print("running supplimental DaisySP compilation flag script")   
