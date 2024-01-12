from bangsue_codename import *

p = BangsueCodename.MRTATrain()
codename = p.get_code_name()

print(p.convert_codename_to_string(codename, "number_with_station"))
