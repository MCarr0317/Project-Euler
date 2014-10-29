<?php
function find_multiples()
{
	$result = 0;
	
	for ($i = 1; $i <= 999; $i++)
	{
		if ($i % 3 == 0 or $i % 5 == 0)
		{
			$result += $i;
		}
	}
	
	return $result;
}

echo find_multiples();
?>
