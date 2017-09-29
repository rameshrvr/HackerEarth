test_case = gets.strip.to_i
limit, array = [], []
(0...test_case).each do |i|
  limit[i] = gets.strip.to_i
  array[i] = gets.strip.split(' ').map(&:to_i)
end

def subarray_sum(arr)
  max = -2000
  arr.sort!
  arr.each_index do |i|
    (i...arr.length).each do |j|
      sum = arr[i..j].inject(0, :+)
      max = sum if sum > max && sum.odd?
    end
  end
  max
end

(0...test_case).map { |index| puts subarray_sum(array[index]) }
