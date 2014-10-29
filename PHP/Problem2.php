<?php
function fibonacci()
{
	$buffer = 0;
	$first = 1;
	$second = 2;
	$current = $first + $second;
	$sum = 2;

	
	while ($current <= 4000000)
	{
		if ($current % 2 == 0)
		{
			$sum += $current;
		}
		$buffer = $second;
		$first = $second;
		$second = $current;
		$current += $buffer;
	}
	
	return $sum;
}

echo fibonacci();
?>
