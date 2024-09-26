using UnityEngine;

namespace uitest
{
    public class UiTestInterface : MonoBehaviour
    {
        private static UiTestInterface instance;
        
        private void Start()
        {
            if (instance != null) return;
            instance = this;
            DontDestroyOnLoad(gameObject);
        }

        public static void BeforeAll()
        {
            Debug.Log("Ui Tests are running");
        }
        
        public static void AfterAll()
        {
            Debug.Log("Ui Tests have completed");
        }
    }
}