string = gets.strip.split('')
duplicate = string.join('')
array = []
(1..string.length).each do
	temp = string.pop
	array.push(temp)
end
array.join('') == duplicate ? (puts "YES") : (puts "NO")