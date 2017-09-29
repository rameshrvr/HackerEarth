test_cases = gets.strip.to_i
array = []
(0...test_cases).each do |i|
  array[i] = gets.strip.split(' ').map(&:to_i)
end

array.each_index do |index|
  sum = array[index].pop
  res = 0
  array[index].sort!
  array[index][1].downto(1).each do |i|
    array[index][0].downto(1).each do |j|
      temp = i * j
      if temp <= sum
        res = temp
        @len = j
      end
      break unless res.zero?
    end
    break unless res.zero?
  end
  set = 1
  array[index][0].downto(@len + 1).each do |i|
    array[index][1].downto(1).each do |j|
      temp = i * j
      if temp > res && temp <= sum
        res = temp
        set = 0
        break
      end
      break if set.zero?
    end
  end
  puts res
end
