import re


def main(s):
    pattern = r"#(.*?) *\|> *`(.*?)\.+"                  # black magic sorcery (regex)
    parsed_s = re.findall(pattern, s.replace('\n', ''))  # parse data into tuple list
    return {key: int(value) for value, key in parsed_s}  # put data into dictionary


# --- cut this out when submitting to robot ---
expr1 = (
    "<block> <data> declare #1474|> `edce. </data>."
    "<data>declare#-4186|>`riquer.</data>. "
    "<data> declare#3755 |> `diquon_733.</data>."
    "<data>declare#-4726 |> `bela. </data>. </block>"
)
expr2 = (
    "<block> <data>declare #-5498|> `edus. </data>. "
    "<data>declare #-1339|>`ontila. </data>. "
    "<data>declare#-9597 |> `recela_196. </data>."
    "<data> declare #-2563 |> `raoner_884.</data>. </block>"
)

print(main(expr1))
print(main(expr2))
