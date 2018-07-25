import sys

def make_list(prompt):
	assert(isinstance(prompt, str))
	l = []
	print("give {}. (give `` to end):".format(prompt))
	while True:
		sys.stdout.write('+ ')
		sys.stdout.flush()
		x = input().strip()
		if x == "":
			print("got {}".format(l))
			return l
		l.append(x)


print("\nSTEP 1. LISTING MOVIES")
movies = make_list("movies")
	
print("\nSTEP 2. LISTING PARTICIPANTS")
participants = make_list("participants")

print("\nSTEP 3. RATINGS")
ratings = {}
for p in participants:
	print("\nRATINGS FOR {}".format(p))
	tot = 0.0
	v_min = 9999999999
	v_max = -99999999
	d = {}
	for m in movies:
		while True:
			try:
				sys.stdout.write("? rating of {} for {}:\t".format(p, m))
				sys.stdout.flush()
				r = float(input().strip())
				#assert(r > 0.)
				break
			except AssertionError as e:
				print("more than 0 please")
			except ValueError as e:
				print("please input some float number!")
		d[m] = r
		v_min = min(v_min, r)
		v_max = max(v_max, r)
		tot += r
	inrange = max(v_max - v_min, 0.00000001)
	
	print("your ratings:", d)
	d2 = {}
	for (k, v) in d.items():
		d2[k] = ((v - v_min)/inrange)*9.0 + 1.0
	print("your ratings normalized:", d2)
	ratings[p] = d2
	
scores = {}
for m in movies:
	score = 1.0
	for p in participants:
		score *= ratings[p][m]
	scores[m] = score
print("\n===================\nFINAL SCORES")
for k,v in sorted(scores.items(), key=lambda x: -x[1]):
	print("{}\t{}".format(round(v), k))