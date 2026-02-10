sample_bay = ["Basalt", "Silica", "Iron", "Dust"]
print(sample_bay[0])
print(sample_bay[-1])
print(len(sample_bay))

for sample in sample_bay:
    print(f"Transmitting data for: {sample}")


new_findings = []
for _ in range(3):
    rock = input("Enter a rock type : ")
    new_findings.append(rock)
print(new_findings) 
