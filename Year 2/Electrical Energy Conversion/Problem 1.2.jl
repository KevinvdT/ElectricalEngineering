# Kevin van der Toorn; Sep 1, 2021
# Script that calculates solutions of Problem 1.2
# of https://homepage.tudelft.nl/80x3n/ee2e11/introduction.html#energy-conversion-architecture-and-efficiency

# Linear regulators, Centralized
v = [15 12 5 3.3]
p = [13 18 15 10]
i = p ./ v
Δv = 18 .- v
p_loss = sum(Δv .* i) # 95.1 W
p_in = 18 * sum(i) # 151 W
p_out = p_in - p_loss 
η = p_out / p_in
println("Linear regulators, centralized η = ", round(η * 100, digits=2), "%")

# Linear regulators, Decentralized
Δv = [18-v[1] v[1]-v[2] v[2]-v[3] v[3]-v[4]]
p_loss = 0
for it in 1:4
    global p_loss += Δv[it] * sum(i[it:4])
end
p_loss # 95.1 W
η = p_out / p_in
println("Linear regulators, decentralized η = ", round(η * 100, digits=2), "%")

# Switchmode converters, Centralized
η = 0.96
println("Switchmode converters, centralized η = ", round(η * 100, digits=2), "%")

# Switchmode converters Decentralized
p_in = sum([p[n]/0.96^n for n in 1:length(p)])
p_out = sum(p)
η = p_out / p_in
println("Switchmode converters, decentralized η = ", round(η * 100, digits=2), "%")
