with open('app.log','r') as f:
    content=f.read()
print(content)

if "INFO" in content :
    info_count=content.count("INFO")
if 'WARNING' in content:
    warning_count=content.count("WARNING")
if "ERROR" in content:
    error_count=content.count('ERROR')

output = (
    f"INFO count: {info_count}\n"
    f"WARNING count: {warning_count}\n"
    f"ERROR count: {error_count}\n"
)
print(output)

with open('log_summary.txt','x')as output_file:
    output_file.write(output)


