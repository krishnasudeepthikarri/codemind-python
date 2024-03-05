l,b,w,c=map(int,input().split())
area_in=l*b
out_l=l+(2*w)
out_b=b+(2*w)
area_out=out_l*out_b
area=area_out-area_in
print(area*c)