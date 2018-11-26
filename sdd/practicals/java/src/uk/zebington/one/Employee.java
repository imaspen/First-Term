package uk.zebington.one;

/**
 * Employee Model
 *
 * @author Aspen Thompson
 */
public class Employee {

    private int id;
    private String name;
    private String jobTitle;
    private String manager;
    private int salary;

    public Employee() {
    }

    public Employee(int id, String name) {
        this.id = id;
        this.name = name;
    }

    public Employee(int id, String name, String jobTitle, String manager, int salary) {
        this.id = id;
        this.name = name;
        this.jobTitle = jobTitle;
        this.manager = manager;
        this.salary = salary;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getJobTitle() {
        return jobTitle;
    }

    public void setJobTitle(String jobTitle) {
        this.jobTitle = jobTitle;
    }

    public String getManager() {
        return manager;
    }

    public void setManager(String manager) {
        this.manager = manager;
    }

    public int getSalary() {
        return salary;
    }

    public void setSalary(int salary) {
        this.salary = salary;
    }

    public void giveSalaryRaise(int percentRaise) {
        this.salary += (this.getSalary() * (percentRaise / 100.0));
    }

    public String parkingPermitStatus() {
        if ((this.jobTitle.startsWith("Senior")) && (this.getSalary() > 22000)) {
            return "Employee is permitted a car parking space.";
        } else {
            return "Employee is not permitted a car parking space.";
        }
    }

    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder("Employee{");

        sb.append("id=").append(id);
        sb.append(", name='").append(name).append('\'');
        sb.append(", jobTitle='").append(jobTitle).append('\'');
        sb.append(", manager='").append(manager).append('\'');
        sb.append(", salary=").append(salary);
        sb.append('}');

        return sb.toString();
    }

    public static void main(String[] args) {
        System.out.println("Creating employee");
        Employee jane = new Employee(123, "Jane Smith");
        System.out.println(jane);

        System.out.println("\nSetting salary");
        jane.setSalary(24000);
        System.out.println(jane);

        System.out.println("\nSetting manager");
        jane.setManager("Barbara Forbes");
        System.out.println(jane);

        System.out.println("\nGiving 5% raise");
        jane.giveSalaryRaise(5);
        System.out.println(jane);

        System.out.println("\nJane's salary is £" + jane.getSalary());

        System.out.println("\nSetting job title");
        jane.setJobTitle("Senior Account Executive");
        System.out.println(jane);

        System.out.println("\nGetting parking permit status");
        System.out.println(jane.parkingPermitStatus());
    }
}
