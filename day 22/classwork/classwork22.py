list1 = ['vashli','msxali']
         
num1=len(list1)
print(num1)

list1.append('cherry')
print(list1)

#lens tvlis siashi elementebis raodenobas
#append amatebs elements siis boloshi

list1.insert(2,'vashli')

print(list1)

list1.pop(1)
print(list1)

#popit index sashualebit vshlit wevrs
#removit tviton mnishvnelobit vshlit
list1.remove('vashli')
print(list1)

#.clear() shlis yvela elements
#.index(value) gvachvenebs ra indexze dgas es nishvneloba
#.count(value) gvitvlis ramdeni es wevria siashi
#.sort() sashualebas gvadzlevs davalagot anbanis an zrdadobis mixedvit
#tu gavaketebt aset ragacas .sort(reverse=True)
print(list1[::-1])

