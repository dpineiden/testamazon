#!/usr/bin/python3


class Chain:
	def __init__(self):
		self.chain=""
		self.out=True
		self.out_element=[]
		self.out_compared=[]

	def set_chain(self,chain):
		self.chain=chain

	def analysis(self):
		B=self.chain.split(";")
		chain_0=B[0]
	
		l=len(B)
		inchain = chain_0
		counter=0
		position=0;
		print(inchain.split('-')[1] == 'END')
		print(counter==0)
		while counter <= l+1:	
			splited_inchain=inchain.split('-')
			if splited_inchain[1].isdigit():
					for k in range(l):
						if splited_inchain[1]==B[k].split('-')[0]:
							position=k;
							break;
					print(inchain)
					inchain=B[position]
					counter +=1
			elif splited_inchain[1] == 'END' and counter==0:
					print(inchain.split('-')[0])
					inchain=B[position+1]
					counter +=1
			else:
				break;
	

		for b in range(l):
			#print(str(B[b])+" "+str(b))
			element=B[b]
			C= element.split('-')
			#print(C)
			reverse_b = C[1]+"-"+C[0]
			compare=True
			if C[0]==C[1]:
				compare=False			
			self.out_element.append(compare)
			G=list(B)
			#print(G)
			G.pop(b)
			for v in range(l-1):
				pre_out_v=True
				#print(reverse_b+" "+G[v])
				if reverse_b==G[v]:
					pre_out_v=False
				self.out_compared.append(pre_out_v)

		#verify chain
		

		#compare boolean array
		result_a=True
		result_b=True				
		for b in range(len(self.out_compared)):
				result_a &= self.out_compared[b]
		for b in range(len(self.out_element)):
				result_b &= self.out_element[b]
		result_c=False
		print(str(counter))		
		if counter>l-1 and counter<=l: 
			result_c=True		

		result_d=False
		if self.chain.find("END"):
			result_d=True
		self.out &= result_a & result_b & result_c & result_d


	

		
			
