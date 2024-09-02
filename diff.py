from parser import parseF
import difflib

class FDiffs:
    def __init__(self, file1, file2):
        self.f1 = parseF(file1)
        self.f2 = parseF(file2)
        self.TotBlocksDiff = len(self.f1) - len(self.f2)
        # self.diffs = difflib.ndiff(self.f1.compressBlocks(), self.f2.compressBlocks())
        self.diffs = []
        dff = {}
        for i in difflib.unified_diff(self.f1.compressBlocks(), self.f2.compressBlocks(), file1, file2, n=0):
            if i.startswith('---') or i.startswith('+++'):
                continue
            elif i.startswith('@@'):
                if dff:
                    # difflib.ndiff(dff['f1Lines'][0].split(), dff['f2Lines'][0].split())
                    dff['Changes'] = []
                    prevplus = []
                    prevms = []
                    diffs = lambda flns1, flns2, char: ''.join(('^^^' if i[0] == char else ('   ' if i[0] == ' ' else '')) for i in difflib.ndiff(flns1.split(), flns2.split()))
                    for j in difflib.ndiff(dff['f1Lines'], dff['f2Lines']):
                        if j.startswith('?'):
                            if len(prevplus) >= 1 and len(prevms) >= 1:
                                ln1 = prevplus.pop(0)[2:]
                                ln2 = prevms.pop(0)[2:]
                                dff['Changes'].append([ln1, diffs(ln1, ln2, '-'), ln2, diffs(ln1, ln2, '+')])
                        elif j.startswith('+'):
                            prevplus.append(j)
                        elif j.startswith('-'):
                            prevms.append(j)
                    if prevplus != [] and prevms != []:
                       for _ in range(min(len(prevplus), len(prevms))):
                            ln1 = prevplus.pop(0)[2:]
                            ln2 = prevms.pop(0)[2:]
                            dff['Changes'].append([ln1, diffs(ln1, ln2, '-'), ln2, diffs(ln1, ln2, '+')])

                    self.diffs.append(dff)
                dff = {}
                bln1 = i.split(' ')[1]
                if ',' in bln1:
                    dff['f1BlockNum'] = int(bln1[1:bln1.index(',')])
                else:
                    dff['f1BlockNum'] = int(bln1[1:])
                bln1 = i.split(' ')[2]
                if ',' in bln1:
                    dff['f2BlockNum'] = int(bln1[1:bln1.index(',')])
                else:
                    dff['f2BlockNum'] = int(bln1[1:])
            elif i.startswith('-'):
                if 'f1Lines' in dff:
                    dff['f1Lines'].append(i[1:])
                else:
                    dff['f1Lines'] = [i[1:]]
            elif i.startswith('+'):
                if 'f2Lines' in dff:
                    dff['f2Lines'].append(i[1:])
                else:
                    dff['f2Lines'] = [i[1:]]
    
    def __str__(self):
        return '<Diff object>'
    def __repr__(self): return self.__str__()

if __name__ == '__main__':
    d = FDiffs('Sample uf2 files/arcade-test.uf2', 'Sample uf2 files/arcade-test(1).uf2')
    pass
