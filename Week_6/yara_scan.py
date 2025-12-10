import yara
# I do not know what to do for sample as i dont want to push an .exe ad github could flag it as dangerous 
sample = r"C:\Users\soubh\Downloads\Procmon.exe"
# YARA scanning
rule = yara.compile(source="""
rule ContainsHTTP {
    strings: $s = "http"
    condition: $s
}
""")

print("Matches:", rule.match(sample))
