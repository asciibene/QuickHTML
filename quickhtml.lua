-- Quick Html 
-- parse a file and output some sort of html from it 

function parseline(lnstr) 
-- takes a line as str and return a copy with markup 
-- rrplaced by html blabla 
  for ic = 1,#lnstr do 
    if (lnstr[ic]=="*" and lnstr[ic+1]=="*") then 
    end 
  end 
end 

cls() 
pdir = droid.primaryvolume() 
infn=pdir.."/test.txt" 
outfn=pdir.."test.html" 
outfn=pdir.. 
fp = io.open(infn, "r") 
-- Capital 'L' sets reading one line WITH newline at the end 
tt = fp:read("L") 
fp:close() 
