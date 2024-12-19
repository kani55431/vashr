import math
from datetime import datetime, timedelta, time
from django.utils.timezone import make_aware, is_naive
from collections import defaultdict
from datetime import datetime, timedelta, time
from django.shortcuts import render, redirect
from django.utils.timezone import make_aware, is_naive

def calculate_shift(intime, outtime, category):
    """Calculate shift based on intime, outtime, and category."""
    if not intime or not outtime:
        return 'NA'
    
    if category.name in ['OFFICE STAFF', 'SUB STAFF']:
        return 'G'
        
    shift = 'Punch Missing'
    
    if category.name == 'SECURITY':
        intime_hour = float(intime.strftime('%H'))  # Convert hour to float in 24-hour format
        outtime_hour = float(outtime.strftime('%H'))  # Convert hour to float in 24-hour format
        
        if intime_hour >= 12 and outtime_hour < 12:
            shift = '2'
        else:
            shift = '1'
    
    elif category.name == 'WORKERS-I':
        intime_hour = float(intime.strftime('%H')) + float(intime.strftime('%M')) / 60  # Convert hour to float with minutes

        if 23.75 <= intime_hour or intime_hour < 7.75:
            shift = '3'
        elif 7 <= intime_hour < 16:
            shift = '1'
        elif 15 <= intime_hour < 24:
            shift = '2'
    
    elif category.name == 'WORKERS-II':
        intime_hour = float(intime.strftime('%H'))  # Convert hour to float in 24-hour format
        
        if intime_hour < 7.9:
            shift = '3'
        elif 8 <= intime_hour < 16:
            shift = '1'
        elif 16 <= intime_hour < 24:
            shift = '2'
    
    return shift

from datetime import datetime, timedelta

def calculate_total_working_hours(intime, outtime):
    """Calculate total working hours between intime and outtime."""
    if intime and outtime:
        # Ensure intime and outtime are aware datetime objects
        intime = make_aware(intime) if is_naive(intime) else intime
        outtime = make_aware(outtime) if is_naive(outtime) else outtime

        # Calculate total seconds
        total_seconds = (outtime - intime).total_seconds()

        if total_seconds < 0:
            total_seconds += 24 * 3600  # Adjust for negative seconds if outtime is on the next day

        # Convert total seconds to hours and minutes
        total_minutes = total_seconds / 60
        hours = int(total_minutes // 60)
        minutes = int(total_minutes % 60)

        # Convert minutes to a fraction of an hour
        decimal_hours = hours + (minutes / 60)
        
        return round(decimal_hours, 2)  # Round to 2 decimal places
    
    return 0.00
from datetime import datetime, timedelta
import math

def calculate_ot_hours(total_working_hours, fixed_working_hours):
    """Calculate overtime hours based on total working hours and fixed working hours."""
    # Ensure the inputs are numeric
    total_working_hours = float(total_working_hours)
    fixed_working_hours = float(fixed_working_hours)
    
    # Calculate the raw overtime hours
    ot_hours = max(total_working_hours - fixed_working_hours, 0)
    
    # Extract hours and minutes from ot_hours
    ot_hours_int = int(ot_hours)
    ot_minutes = (ot_hours - ot_hours_int) * 60  # Convert the fractional hour part to minutes
    
    # Apply the rounding rule: if minutes are 45 or more, round up to the next hour, otherwise round down
    if ot_minutes >= 45:
        rounded_ot_hours = ot_hours_int + 1
    else:
        rounded_ot_hours = ot_hours_int
    
    return rounded_ot_hours  # Return as an integer (whole number)


def get_workday(log_datetime, category):
    """Determine the workday for a given log datetime based on category."""
    if category.name in ['WORKERS-I', 'WORKERS-II', 'SECURITY']:
        if log_datetime.time() < time(9, 0):
            return (log_datetime - timedelta(days=1)).date()
    return log_datetime.date()
