PLACEHOLDER = "[name]"

with (
    open(file="template_and_names/template.txt", mode="r") as template_file,
    open(file="template_and_names/names.txt", mode="r") as names_file
):
    template = template_file.read()
    names = names_file.readlines()

for name in names:
    name = name.strip()
    temp_up = template.replace(PLACEHOLDER, name)

    with open(file=f"output/{name}_letter.txt", mode="w") as out_file:
        out_file.write(temp_up)
