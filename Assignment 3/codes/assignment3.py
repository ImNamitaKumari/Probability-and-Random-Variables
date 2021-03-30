from matplotlib_venn import venn2
# defining our venn
#subsets has 3 arguments (a,b,c), a is P(AB'), b is P(A'B), c is P(AB)
#A is the universe as P(A)=1, P(B)=0.5 So, P(AB)=0.5
v = venn2(subsets=(0.5,0,0.5), set_labels = ('Set A', 'Set B'))
