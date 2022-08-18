Di = {
    1: "¹",
    2: "²",
    3: "³",
    4: "⁴",
    5: "⁵",
    6: "⁶",
    7: "⁷",
    8: "⁸",
    9: "⁹",
    0: "⁰"
}

def nig(ga):
    ret = ""
    for i in str(ga):
        ret += Di[int(i)]
    return ret

stri = ""
n, i = 0, -2
while n <= 2:
    try:
        n = int(input("==> "))
    except ValueError:
        print ("Atleast 3")

print ("x¹")
stri += "x¹"
while i != (3*n - 8):
    i += 3
    print (f"∀x{nig(i+1)}(x{nig(i+1)}∈x{nig(i)}⇔((∀x{nig(i+2)}(x{nig(i+2)}∈x{nig(i+1)}⇔x{nig(i+2)}∈x{nig(i+3)})∨x{nig(i+1)}∈x{nig(i+3)})∧")
    stri += f"∀x{nig(i+1)}(x{nig(i+1)}∈x{nig(i)}⇔((∀x{nig(i+2)}(x{nig(i+2)}∈x{nig(i+1)}⇔x{nig(i+2)}∈x{nig(i+3)})∨x{nig(i+1)}∈x{nig(i+3)})∧"

print (f"∀x{nig(i+4)}(x{nig(i+4)}∈x{nig(i+3)}⇔(¬∃x{nig(i+5)}(x{nig(i+5)}∈x{nig(i+4)})∨∀x{nig(i+5)}(x{nig(i+5)}∈x{nig(i+4)}⇔¬∃x{nig(i+6)}(x{nig(i+6)}∈x{nig(i+5)}))))")
stri += f"∀x{nig(i+4)}(x{nig(i+4)}∈x{nig(i+3)}⇔(¬∃x{nig(i+5)}(x{nig(i+5)}∈x{nig(i+4)})∨∀x{nig(i+5)}(x{nig(i+5)}∈x{nig(i+4)}⇔¬∃x{nig(i+6)}(x{nig(i+6)}∈x{nig(i+5)}))))"
print(")"*int((2*i+4)/3))
stri += ")"*int((2*i+4)/3)

print ("\n\n\n")
print (stri)
