def delete(self, val):
	if self is None:
		return None
	
	else:
		if val < self.data:
			self.left = self.left.delete(val)
		elif val > self.data:
			self.right = self.right.delete(val)
		else:
			//case1
			if self.left is None and self.right is None: 
				return None
			//case2
			if self.left is None:
				return self.right
			if self.right is None:
				return self.left
			
			temp = self.right
			while temp.left:
				temp = temp.left
				
			self.data = temp.data
			self.right = self.right.delete(temp.data)
			
		return self
			
			
			
