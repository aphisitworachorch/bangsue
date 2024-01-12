![Bangsue_Image](https://github.com/aphisitworachorch/bangsue/blob/master/bangsue.jpg)

# Bangsue
Thai Codename Generator (Data from data.go.th)

## Installation

    pip install bangsue
 ---
 ##  Example Code
 
    from bangsue_codename import *
    p = BangsueCodename.ThailandDistrict()
    codename = p.get_code_name()
    print(p.convert_codename_to_string(codename, "all"))
    
    RESULT : khaoyai_aoluek_krabi