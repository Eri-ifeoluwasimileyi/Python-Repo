world_population = 8_062_000_000

growth_rate = 0.0085


for years in range(1, 101):
		
	world_population = (world_population * growth_rate) + world_population

			
	print(f'{years:2}	{world_population:.3f}		{world_population * growth_rate:>3}')