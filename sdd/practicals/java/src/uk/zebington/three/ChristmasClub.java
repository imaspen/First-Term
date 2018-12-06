package uk.zebington.three;

import java.util.ArrayList;

public class ChristmasClub {

    private ArrayList<Member> Members;

    public ChristmasClub() {
        this.Members = new ArrayList<Member>();
    }

    public void addMember(Member newMember) {
        this.Members.add(newMember);
    }

    /**
     * Iterates over the Members ArrayList and gets each member's contribution, returning the total.
     * @return the sum of all members contributions
     */
    public int getTotalContributions() {
        int total = 0;
        for (Member member : Members) {
            total += member.getContribution();
        }
        return total;
    }

    /**
     * Get's the total contributions and divides it by the turkey price of 20, integer division rounding down.
     * @return the total turkeys that can be purchased based on the Members' contributions
     */
    public int getAvailableTurkeys() {
        return getTotalContributions() / 20;
    }

    public String toString() {
        String s = "";

        s = "Current Members\n\n";

        for (Member c : this.Members) {
            s += c.toString();
            s += "\n";
        }

        return s;
    }

    public static void main(String[] args) {

        Member gary = new Member("Gary", 27);
        Member tony = new Member("Tony", 21);
        Member rubiya = new Member("Rubiya", 20);
        Member steve = new Member("Steve", 28);

        ChristmasClub myMembers = new ChristmasClub();

        myMembers.addMember(gary);
        myMembers.addMember(tony);
        myMembers.addMember(rubiya);
        myMembers.addMember(steve);

        System.out.println(myMembers);

        System.out.println("Total contributions made: £" + myMembers.getTotalContributions() + ".");

        System.out.println("Total number of turkeys available: " + myMembers.getAvailableTurkeys() + ".");
    }
}
