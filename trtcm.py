def trTCM(Tc, Tp, B, CIR, PIR, CBS, PBS):
    """
    Implements the Two Rate Three Color Marker (trTCM) algorithm.
    Marks the packet as green, yellow, or red.
    """
    # Tokens are replenished at a rate of 1/CIR for Tc and 1/PIR for Tp per second.
    # Assuming a tick happens each time this function is called.
    increment_c = 1 / CIR
    increment_p = 1 / PIR

    # Increment tokens if not at burst size limits
    if Tc < CBS:
        Tc = min(Tc + increment_c, CBS)
    if Tp < PBS:
        Tp = min(Tp + increment_p, PBS)

    # Compare packet size with token count of Bucket P first
    if Tp >= B:
        # If Bucket P has enough tokens, compare with Bucket C
        if Tc >= B:
            # Both buckets have enough tokens, packet is marked green
            Tc -= B
            Tp -= B
            color = 'Green'
        else:
            # Only Bucket P has enough tokens, packet is marked yellow
            Tp -= B
            color = 'Yellow'
    else:
        # Bucket P does not have enough tokens, packet is marked red
        color = 'Red'

    return Tc, Tp, color

def main_trTCM():
    """
    Main function to run the trTCM algorithm with an example packet.
    """
    # Set the rates and sizes
    CIR = 1000  # bytes per second
    PIR = 2000  # bytes per second
    CBS = 100   # bytes
    PBS = 200   # bytes

    # Initial token counts for Bucket C and Bucket P
    Tc, Tp = 80, 150  # bytes

    # Size of the incoming packet
    B = 8  # bytes

    # Run the trTCM algorithm
    Tc, Tp, color = trTCM(Tc, Tp, B, CIR, PIR, CBS, PBS)

    # Print the results
    print(f"After processing a packet of {B} bytes:")
    print(f"Token count for Bucket C (Tc): {Tc}")
    print(f"Token count for Bucket P (Tp): {Tp}")
    print(f"Packet is marked as: {color}")

# Call the main function
main_trTCM()
