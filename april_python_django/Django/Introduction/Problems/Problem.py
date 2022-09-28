results = [
    {"district":"tvm","win": 98, "A+": 45000},
    {"district":"ktm","win": 95, "A+": 44000},
    {"district":"apy","win": 97, "A+": 47000},
    {"district":"idk","win": 90 ,"A+": 38000},
    {"district":"ekm","win": 99, "A+": 56000},
    {"district":"pta","win": 99, "A+": 58000},
    {"district":"tsr","win": 98, "A+": 57000},
    {"district":"kzd","win": 99, "A+": 58000},
    {"district":"pkd","win" :95, "A+": 50000},
    {"district":"mpm","win": 90,"A+": 4500},

]

#Win % tvm

#

# for result in results:
#     if result["district"]=="tvm":
#         print(result["win"])
tvm_win=[result["win"] for result in results if result["district"]=="tvm"]
print(tvm_win)

# Sort with win%
results.sort(key=lambda res:res["win"], reverse=True)
print(results)
#dis with highest win%
print(max(results,key=lambda res:res["win"]))
#dis with lowest win%
print("Lowest win rate at:",min(results,key=lambda res:res["win"]))
#highest aplus
print(max(results,key=lambda res:res["A+"]))
#lowest aplus
print(min(results,key=lambda res:res["A+"]))
#sum of A+
a_plus=sum([res["A+"] for res in results])
print(a_plus)