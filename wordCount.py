# IDK why I hate grammar so much
import sys

def main(fIN, fOUT):
    f = open(fIN,'r')
    content = []
    for x in f:
        if '-' in x:
            lef = x[:x.index('-')]
            rig = x[x.index('-')+1:]
            content.extend(lef.split()+rig.split())
        elif "'" in x:
            lef = x[:x.index("'")]
            rig = x[x.index("'")+1:]
            content.extend(lef.split()+rig.split())
        else:
            content.extend(x.split())
    f.close
    unique = {}
    for x in content:
        x = ''.join(i for i in x if i not in ('?','.',',',';',':','!','"',"'",'-'))
        x = x.lower()
        if x in unique:
            unique.update({x:unique[x]+1})
        else: unique[x] = 1
    f = open(fOUT, 'w')
    sort_unique = sorted(unique.items(), key=lambda x:x[0])
    for x in sort_unique:
        f.write(str(x[0])+' '+str(x[1]))
        f.write('\n')
    f.close()

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])
    
