def hanoi_solver(n): 
    rods = {  
        'A': list(range(n, 0, -1)),  
        'B': [],  
        'C': []  
    }  
    
    history_of_moves = []  
    
    def record_current_state(): 
        current_state = f"{rods['A']} {rods['B']} {rods['C']}"
        history_of_moves.append(current_state)  
        
    record_current_state()  
    
    def move_disks(number_of_disks, source_rod, target_rod, auxiliary_rod):  
        if number_of_disks == 1:  
            disk = rods[source_rod].pop()  
            rods[target_rod].append(disk)  
            record_current_state()  
            return  
            
        move_disks(number_of_disks - 1, source_rod, auxiliary_rod, target_rod)  

        disk = rods[source_rod].pop()  
        rods[target_rod].append(disk) 
        record_current_state() 
        
        move_disks(number_of_disks - 1, auxiliary_rod, target_rod, source_rod)  

    move_disks(n, source_rod='A', target_rod='C', auxiliary_rod='B')  
    
    return '\n'.join(history_of_moves) 