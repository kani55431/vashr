def calculate_shift(intime, outtime, category_name):
    """Calculate shift based on intime, outtime, and category."""
    if not intime or not outtime:
        return 'NA'
    
    if category_name in ['OFFICE STAFF', 'SUB STAFF']:
        return 'G'
        
    if category_name == 'SECURITY':
        intime_hour = float(intime.strftime('%H'))  # Convert hour to float in 24-hour format
        outtime_hour = float(outtime.strftime('%H'))  # Convert hour to float in 24-hour format
        
        if intime_hour >= 20 or (intime_hour < 8 and outtime_hour >= 8):
            return '2'  # Night Shift (8 PM to 8 AM)
        else:
            return '1'  # Day Shift (8 AM to 8 PM)
    
    if category_name in ['WORKERS-I', 'WORKERS-II']:
        intime_hour = float(intime.strftime('%H')) + float(intime.strftime('%M')) / 60  # Convert hour to float with minutes
        
        if 0 <= intime_hour < 8:
            return '3'  # Night Shift (12 AM to 8 AM)
        elif 8 <= intime_hour < 16:
            return '1'  # Day Shift 1 (8 AM to 4 PM)
        elif 16 <= intime_hour < 24:
            return '2'  # Day Shift 2 (4 PM to 12 AM)
    
    return 'NA'
