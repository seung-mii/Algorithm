import java.io.*;
import java.util.*;
 
public class Main {
	public static void main(String[] args) throws IOException {		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		Person[] p = new Person[N];
 
		for(int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int age = Integer.parseInt(st.nextToken());
			String name = st.nextToken();
			p[i] = new Person(age, name);
		}
 
		// 타입을 Person 으로
		Arrays.sort(p, new Comparator<Person>() {
			@Override
			public int compare(Person s1, Person s2) { // 나이 순 정렬
				return s1.age - s2.age;
			}
		});
 
		for(int i = 0; i < N; i++) {
			// 객체 배열의 객체를 출력하면 해당 인덱스의 객체의 toString() 이 출력됨
			System.out.println(p[i]);
		}
	}
    
	public static class Person {
		int age;
		String name;
        
		public Person(int age, String name) {
			this.age = age;
			this.name = name;
		}
        
		@Override
		public String toString() {
			return age + " " + name;
		}
	}
}