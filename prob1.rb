test_cases = gets.strip.to_i
detail, array = Array.new{Array.new}, Array.new{Array.new}
(0..test_cases-1).each do |x|
  detail[x] = gets.strip.split(' ').map{|y| y.to_i}
  array[x] = gets.strip.split(' ').map{|y| y.to_i} unless detail[x][1] == 0
end
result, count = 'Yes', 0
(0..test_cases-1).each do |x|
	(0..detail[x][1]-1).each do |y|
		if detail[x][0] <= 0 && y != (detail[x][1]-1)
			result = 'No'
			break
		end
		array[x][y] == 0 ? detail[x][0] -= 1 : detail[x][0] += 2
		count = y+1
	end
	if detail[x][1] == 0
		result = 'No'
		count = 0
	end
	if result.include? 'Yes'
		puts "#{result} #{detail[x][0]}"
	else
		puts "#{result} #{count}"
	end
end
