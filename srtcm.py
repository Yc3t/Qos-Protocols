# Define all the functions with complete logic as per srTCM algorithm

def rates(CIR):
    """
    Sets the Committed Information Rate.
    """
    return CIR

def burst_sizes(CBS, EBS):
    """
    Sets the Committed Burst Size and Excess Burst Size.
    """
    return CBS, EBS

def srTCM(Tc, Te, B, CIR, CBS, EBS):
    """
    Implements the Single Rate Three Color Marker algorithm.
    Marks the packet as green, yellow, or red.
    """
    # Tokens are replenished at a rate of 1/CIR per second.
    # Assuming a tick happens each time this function is called.
    increment = 1 / CIR

    # Increment tokens if not at burst size limits
    if Tc < CBS:
        Tc = min(Tc + increment, CBS)
    if Te < EBS and Tc == CBS:
        Te = min(Te + increment, EBS)

    # Check if there are enough tokens in bucket C for the packet
    if Tc >= B:
        Tc -= B  # Packet is marked green
        color = 'Green'
    # Check if bucket C is not enough but bucket E has enough tokens
    elif Te >= B:
        Te -= B  # Packet is marked yellow
        color = 'Yellow'
    else:
        # Packet is marked red
        color = 'Red'

    return Tc, Te, color

def main():
    """
    Main function to run the srTCM algorithm with an example packet.
    """
    # Set the rates and sizes
    CIR = rates(1000)  # bytes per second
    CBS, EBS = burst_sizes(100, 200)  # bytes

    # Initial token counts for Bucket C and E
    Tc, Te = 80, 150  # bytes

    # Size of the incoming packet
    B = 8  # bytes

    # Run the srTCM algorithm
    Tc, Te, color = srTCM(Tc, Te, B, CIR, CBS, EBS)

    # Print the results
    print(f"After processing a packet of {B} bytes:")
    print(f"Token count for Bucket C (Tc): {Tc}")
    print(f"Token count for Bucket E (Te): {Te}")
    print(f"Packet is marked as: {color}")

# Call the main function
main()
